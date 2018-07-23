from flask import Flask, render_template,request
import serial
import time

app = Flask(__name__)

@app.route('/')
def index()->str:
	return render_template('index.html')

@app.route('/getpost1', methods = ['GET'])
def getpost1()->str:
	ser = serial.Serial('/dev/ttyACM0',9600)
	time.sleep(2)
	if request.method == 'GET':
		res = request.args.get('get1_value')
		ser.write(b'S8\r')
		ser.write(b'O\r')
		ser.write(b't3018F100500101000000')
		ser.write(b'S8\r')
		ser.write(b'O\r')
	return res
@app.route('/getpost2', methods = ['GET'])
def getpost2()->str:
	ser = serial.Serial('/dev/ttyACM0',9600)
	time.sleep(2)
	if request.method == 'GET':
		res = request.args.get('get2_value')
		ser.write(b'S8\r')
		ser.write(b'O\r')
		ser.write(b't3018F1006C0064000000')
		ser.write(b'S8\r')
		ser.write(b'O\r')
	return res
@app.route('/getpost3', methods = ['GET'])
def getpost3()->str:
        ser = serial.Serial('/dev/ttyACM0',9600)
        time.sleep(2)
        if request.method == 'GET':
                res = request.args.get('get3_value')
                ser.write(b'S8\r')
                ser.write(b'O\r')
                ser.write(b't3018F100510100000000')
                ser.write(b'S8\r')
                ser.write(b'O\r')
        return res

@app.route('/getpost4', methods = ['GET'])
def getpost4()->str:
        ser = serial.Serial('/dev/ttyACM0',9600)
        time.sleep(2)
        if request.method == 'GET':
                res = request.args.get('get4_value')
                ser.write(b'S8\r')
                ser.write(b'O\r')
                ser.write(b't3018F100500100000000')
                ser.write(b'S8\r')
                ser.write(b'O\r')
        return res

if __name__ == '__main__':
	app.run()
