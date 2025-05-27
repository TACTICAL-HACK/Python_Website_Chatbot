from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

data = {
    "Hardware": {
        "Microsoft Surface Device": {
            "Warranty Process": "To check the warranty status, go to this link:\nhttps://mybusinessservice.surface.com/\n\nTo create a support request go to this link:\nhttps://support.serviceshub.microsoft.com/supportforbusiness/manage"
        },
        "Device Troubleshooting": {
            "No Display": "Check HDMI connection. Try a different cable."
        }
    },
    "Software": {
        "Outlook Issue": {
            "Reset Profile": "Go to Control Panel > Mail > Show Profiles > Add new."
        }
    },
    "Printer": {
        "Add Printer": {
            "Network Printer": "Go to Settings > Devices > Printers > Add a printer."
        }
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_root', methods=['GET'])
def get_root():
    return jsonify(list(data.keys()))

@app.route('/get_options', methods=['POST'])
def get_options():
    path = request.json.get('path', [])
    ref = data

    for key in path:
        if isinstance(ref, dict) and key in ref:
            ref = ref[key]
        else:
            return jsonify({"type": "error", "data": ["Invalid selection. Please start over."]})

    if isinstance(ref, str):
        return jsonify({"type": "message", "data": ref})
    return jsonify({"type": "options", "data": list(ref.keys())})

if __name__ == '__main__':
    app.run(debug=True)
