
from flask import Flask, request, jsonify
from hashing.hasher import bcrypt_hash, bcrypt_verify, argon2_hash, argon2_verify
from hashing.strength import check_password_strength

app = Flask(__name__)

# Route: Hash Password
@app.route('/hash', methods=['POST'])
def hash_password():
    """
    API endpoint to hash a password.
    """
    data = request.get_json()
    password = data.get('password')
    if not password:
        return jsonify({"error": "Password is required"}), 400

    # Hash using bcrypt and Argon2
    bcrypt_hashed = bcrypt_hash(password)
    argon2_hashed = argon2_hash(password)

    return jsonify({
        "bcrypt_hashed": bcrypt_hashed,
        "argon2_hashed": argon2_hashed
    })

# Route: Verify Password
@app.route('/verify', methods=['POST'])
def verify_password():
    """
    API endpoint to verify a password against a given hash.
    """
    data = request.get_json()
    password = data.get('password')
    hashed_password = data.get('hashed_password')
    method = data.get('method')

    if not password or not hashed_password:
        return jsonify({"error": "Password and hashed_password are required"}), 400

    if method == "bcrypt":
        is_valid = bcrypt_verify(password, hashed_password)
    elif method == "argon2":
        is_valid = argon2_verify(password, hashed_password)
    else:
        return jsonify({"error": "Invalid hashing method. Use 'bcrypt' or 'argon2'."}), 400

    return jsonify({"is_valid": is_valid})

# Route: Password Strength Check
@app.route('/strength', methods=['POST'])
def password_strength():
    """
    API endpoint to check the strength of a password.
    """
    data = request.get_json()
    password = data.get('password')
    if not password:
        return jsonify({"error": "Password is required"}), 400

    strength_result = check_password_strength(password)
    return jsonify(strength_result)

if __name__ == '__main__':
    app.run(debug=True)
