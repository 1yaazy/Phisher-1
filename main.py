# main.py
from flask import Flask

app = Flask(__name__)

# HTML and CSS as strings
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Aishath Ahmed</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #ff4444 0%, #ffaa00 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .card {
            background: white;
            padding: 30px 25px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            text-align: center;
            width: 100%;
            max-width: 350px;
            min-height: 500px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: center;
            border: 3px solid #ff4444;
            position: relative;
        }
        .heading {
            color: #333;
            margin: 0;
            font-size: 2rem;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            border-bottom: 3px solid #ff4444;
            padding-bottom: 15px;
            margin-top: 10px;
            line-height: 1.2;
        }
        .warning {
            font-size: 2.5rem;
            font-weight: bold;
            text-shadow: 3px 3px 6px rgba(255, 0, 0, 0.3);
            margin-top: 25px;
            background: linear-gradient(45deg, #ff4444, #ffaa00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: pulse 2s infinite;
        }
        .text-box {
            margin-top: 30px;
            padding: 15px;
            background: #f8f8f8;
            border: 2px solid #ff4444;
            border-radius: 8px;
            color: #333;
            font-size: 1rem;
            font-weight: 500;
            width: 100%;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            line-height: 1.4;
        }
        .border-mark {
            position: absolute;
            font-size: 1.2rem;
            font-weight: bold;
            color: #000000;
        }
        
        /* Fixed rotations - no animation */
        .mark-1 { top: 8px; left: 15px; transform: rotate(-15deg); }
        .mark-2 { top: 8px; right: 15px; transform: rotate(25deg); }
        .mark-3 { bottom: 8px; left: 15px; transform: rotate(10deg); }
        .mark-4 { bottom: 8px; right: 15px; transform: rotate(-20deg); }
        .mark-5 { top: 50%; left: 3px; transform: rotate(-45deg) translateY(-50%); }
        .mark-6 { top: 50%; right: 3px; transform: rotate(45deg) translateY(-50%); }
        .mark-7 { top: 25%; left: 3px; transform: rotate(-30deg); }
        .mark-8 { top: 25%; right: 3px; transform: rotate(30deg); }
        .mark-9 { bottom: 25%; left: 3px; transform: rotate(30deg); }
        .mark-10 { bottom: 25%; right: 3px; transform: rotate(-30deg); }
        .mark-11 { top: 60px; left: 50%; transform: rotate(15deg) translateX(-50%); }
        .mark-12 { bottom: 60px; left: 50%; transform: rotate(-15deg) translateX(-50%); }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }

        /* Mobile responsiveness */
        @media (max-width: 480px) {
            body {
                padding: 15px;
            }
            .card {
                padding: 25px 20px;
                min-height: 450px;
            }
            .heading {
                font-size: 1.8rem;
            }
            .warning {
                font-size: 2.2rem;
            }
            .text-box {
                font-size: 0.95rem;
                padding: 12px;
            }
            .border-mark {
                font-size: 1rem;
            }
        }

        @media (max-width: 360px) {
            .heading {
                font-size: 1.6rem;
            }
            .warning {
                font-size: 2rem;
            }
            .text-box {
                font-size: 0.9rem;
            }
        }
    </style>
</head>
<body>
    <div class="card">
        <h1 class="heading">Hello Aishath Ahmed</h1>
        <div class="warning">!</div>
        
        <!-- Text Box - Change the text below by editing this file -->
        <div class="text-box">
            This is my editable text box! I can change this text anytime by editing the Python code.
        </div>
        
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
