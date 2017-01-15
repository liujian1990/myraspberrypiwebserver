from flaskr import flaskr
try:
    flaskr.app.run(host='0.0.0.0', port=80)
except Exception,e:
    print "[*] error:",e
