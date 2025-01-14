from flask import Flask, request, jsonify
from hashing.hasher import bcrypt_hash, bcrypt_verify, argon2_hash, argon2_verify
from hashing.strength import check_password_strength

app = Flask(__name__)

# ✅ Root Route
@app.route('/')
def home():
    return """
    <h1>Welcome to SecurePass Hashing Service!</h1>
    <p>Available Endpoints:</p>
    <ul>
        <li><strong>/hash</strong> - POST: Hash a password using bcrypt and argon2</li>
        <li><strong>/verify</strong> - POST: Verify a hashed password</li>
        <li><strong>/strength</strong> - POST: Check password strength</li>
    </ul>
    """

# Route: Hash Password
@app.route('/hash', methods=['POST'])
def hash_password():
    data = request.get_json()
    password = data.get('password')
    if not password:
        return jsonify({"error": "Password is required"}), 400

    bcrypt_hashed = bcrypt_hash(password)
    argon2_hashed = argon2_hash(password)

    return jsonify({
        "bcrypt_hashed": bcrypt_hashed,
        "argon2_hashed": argon2_hashed
    })

# Route: Verify Password
@app.route('/verify', methods=['POST'])
def verify_password():
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

# Route: Password Strength
@app.route('/strength', methods=['POST'])
def password_strength():
    data = request.get_json()
    password = data.get('password')
    if not password:
        return jsonify({"error": "Password is required"}), 400

    strength_result = check_password_strength(password)
    return jsonify(strength_result)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
