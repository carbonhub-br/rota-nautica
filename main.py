from flask import Flask, request, jsonify
import searoute as sr

app = Flask(__name__)

@app.route('/route')
def route():
    try:
        flat = float(request.args['flat'])
        flon = float(request.args['flon'])
        tlat = float(request.args['tlat'])
        tlon = float(request.args['tlon'])
    except (KeyError, ValueError):
        return jsonify({'error': 'Params: flat, flon, tlat, tlon required'}), 400

    try:
        result = sr.searoute([flon, flat], [tlon, tlat])
        props  = result['properties']
        coords = result['geometry']['coordinates']  # [[lon, lat], ...]
        latlngs = [[round(c[1], 5), round(c[0], 5)] for c in coords]
        return jsonify({
            'km':     round(props['length'], 1),
            'nm':     round(props['length'] / 1.852, 1),
            'coords': latlngs,
            'pts':    len(latlngs)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'searoute': sr.__version__ if hasattr(sr,'__version__') else 'ok'})

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
