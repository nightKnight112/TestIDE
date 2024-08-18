from flask import Flask, request, jsonify
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/execute-code', methods=['POST'])
def execute_code():
    data = request.json
    container_id = data.get('container-id')
    language = data.get('language')
    codeList = data.get('code')
    code = codeList[0]

    if not container_id or not language or not code:
        return jsonify({"error": "container_id, language, and code are required"}), 400

    try:
        container = client.containers.get(container_id)
        if language == 'python':
            # Execute Python code directly via stdin
            result = container.exec_run(['python3', '-c', code])
        elif language == 'java':
            # Handle Java code by writing to stdin, compiling, and running
            java_command = f'echo "{code}" > Main.java && javac Main.java && java Main'
            result = container.exec_run(['sh', '-c', java_command])
        else:
            return jsonify({"error": "Unsupported language"}), 400

        return jsonify({"output": result.output.decode('utf-8')}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
