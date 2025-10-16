# main.py
from flask import Flask

app = Flask(__name__)

# HTML and CSS as strings
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Aishath Ahmed</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #ff4444 0%, #ffaa00 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .card {
            background: white;
            padding: 60px 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            text-align: center;
            max-width: 400px;
            min-height: 500px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: center;
            padding-top: 40px;
            border: 3px solid #ff4444;
            position: relative;
        }
        .heading {
            color: #333;
            margin: 0;
            font-size: 3rem;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            border-bottom: 3px solid #ff4444;
            padding-bottom: 20px;
            margin-top: 40px;
        }
        .warning {
            font-size: 3rem;
            font-weight: bold;
            text-shadow: 3px 3px 6px rgba(255, 0, 0, 0.3);
            margin-top: 30px;
            background: linear-gradient(45deg, #ff4444, #ffaa00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: pulse 2s infinite;
        }
        .border-mark {
            position: absolute;
            font-size: 1.5rem;
            font-weight: bold;
            color: #000000;
        }
        
        /* Fixed rotations - no animation */
        .mark-1 { top: 10px; left: 20px; transform: rotate(-15deg); }
        .mark-2 { top: 10px; right: 20px; transform: rotate(25deg); }
        .mark-3 { bottom: 10px; left: 20px; transform: rotate(10deg); }
        .mark-4 { bottom: 10px; right: 20px; transform: rotate(-20deg); }
        .mark-5 { top: 50%; left: 5px; transform: rotate(-45deg) translateY(-50%); }
        .mark-6 { top: 50%; right: 5px; transform: rotate(45deg) translateY(-50%); }
        .mark-7 { top: 25%; left: 5px; transform: rotate(-30deg); }
        .mark-8 { top: 25%; right: 5px; transform: rotate(30deg); }
        .mark-9 { bottom: 25%; left: 5px; transform: rotate(30deg); }
        .mark-10 { bottom: 25%; right: 5px; transform: rotate(-30deg); }
        .mark-11 { top: 80px; left: 50%; transform: rotate(15deg) translateX(-50%); }
        .mark-12 { bottom: 80px; left: 50%; transform: rotate(-15deg) translateX(-50%); }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class="card">
        <h1 class="heading">Hello Aishath Ahmed</h1>
        <div class="warning">!</div>
        
        <!-- Exclamation marks around the border -->
        <div class="border-mark mark-1">!</div>
        <div class="border-mark mark-2">!</div>
        <div class="border-mark mark-3">!</div>
        <div class="border-mark mark-4">!</div>
        <div class="border-mark mark-5">!</div>
        <div class="border-mark mark-6">!</div>
        <div class="border-mark mark-7">!</div>
        <div class="border-mark mark-8">!</div>
        <div class="border-mark mark-9">!</div>
        <div class="border-mark mark-10">!</div>
        <div class="border-mark mark-11">!</div>
        <div class="border-mark mark-12">!</div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML_TEMPLATE

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)