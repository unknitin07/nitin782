<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Jalwa.Game - Register</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background-color: #07071A;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 0;
            color: #EAF6FF;
            overflow-x: hidden;
        }

        /* Header */
        .header {
            width: 100%;
            max-width: 420px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px 20px;
            position: relative;
        }

        .back-button {
            width: 36px;
            height: 36px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.15s ease;
        }

        .back-button:active {
            transform: scale(0.95);
            background: rgba(255, 255, 255, 0.05);
        }

        .back-button svg {
            width: 20px;
            height: 20px;
            stroke: #9BB0CF;
            stroke-width: 2.5;
        }

        .logo {
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            font-size: 20px;
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        .logo-gradient {
            background: linear-gradient(135deg, #1FE1C8 0%, #18D9BE 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .language-selector {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 6px 10px;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            cursor: pointer;
        }

        .flag-icon {
            width: 22px;
            height: 22px;
            border-radius: 3px;
        }

        .language-selector span {
            font-size: 13px;
            font-weight: 600;
            color: #9BB0CF;
        }

        /* Main Card Container */
        .container {
            width: 100%;
            max-width: 420px;
            padding: 0 20px 40px;
        }

        .card {
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.02) 0%, rgba(255, 255, 255, 0.01) 100%);
            background-color: #0B1330;
            border-radius: 18px;
            padding: 20px;
            box-shadow: 0 16px 40px rgba(2, 6, 18, 0.65);
            border: 1px solid rgba(255, 255, 255, 0.02);
        }

        /* Title Section */
        .title-section {
            margin-bottom: 20px;
        }

        .title {
            font-size: 20px;
            font-weight: 700;
            color: #EAF6FF;
            margin-bottom: 6px;
        }

        .subtitle {
            font-size: 13px;
            color: #9BB0CF;
            font-weight: 400;
            margin-bottom: 14px;
        }

        .divider {
            height: 2px;
            background: linear-gradient(90deg, #1FE1C8 0%, rgba(31, 225, 200, 0.08) 100%);
            border-radius: 2px;
        }

        /* Phone Register Section */
        .phone-register {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 24px 0;
        }

        .phone-icon {
            width: 44px;
            height: 44px;
            border-radius: 12px;
            background: rgba(31, 225, 200, 0.08);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
        }

        .phone-icon svg {
            width: 22px;
            height: 22px;
            stroke: #1FE1C8;
            stroke-width: 2;
        }

        .phone-register-text {
            font-size: 15px;
            font-weight: 600;
            color: #1FE1C8;
            letter-spacing: 0.3px;
        }

        /* Form Fields */
        .form-group {
            margin-bottom: 18px;
        }

        .form-label {
            font-size: 13px;
            font-weight: 500;
            color: #9BB0CF;
            margin-bottom: 8px;
            display: block;
        }

        .input-wrapper {
            position: relative;
        }

        .form-input {
            width: 100%;
            height: 56px;
            border-radius: 14px;
            background: linear-gradient(180deg, #071330 0%, #081A38 100%);
            border: 1px solid rgba(255, 255, 255, 0.03);
            box-shadow: inset 0 6px 18px rgba(3, 7, 18, 0.7);
            padding: 0 16px;
            font-size: 15px;
            font-family: 'Poppins', sans-serif;
            color: #E9FBFF;
            transition: all 0.15s ease;
        }

        .form-input::placeholder {
            color: #9BB0CF;
            opacity: 0.6;
        }

        .form-input:focus {
            outline: none;
            border-color: rgba(31, 225, 200, 0.2);
            box-shadow: inset 0 6px 18px rgba(3, 7, 18, 0.7), 0 0 0 1px rgba(31, 225, 200, 0.1);
        }

        /* Phone Number Field */
        .phone-input-group {
            display: flex;
            gap: 10px;
        }

        .country-code {
            width: 88px;
            height: 56px;
            border-radius: 14px;
            background: linear-gradient(180deg, #071330 0%, #081A38 100%);
            border: 1px solid rgba(255, 255, 255, 0.03);
            box-shadow: inset 0 6px 18px rgba(3, 7, 18, 0.7);
            padding: 0 12px;
            font-size: 15px;
            font-family: 'Poppins', sans-serif;
            color: #E9FBFF;
            cursor: pointer;
            appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg width='12' height='8' viewBox='0 0 12 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1.5L6 6.5L11 1.5' stroke='%239BB0CF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 12px center;
            padding-right: 32px;
        }

        .country-code:focus {
            outline: none;
            border-color: rgba(31, 225, 200, 0.2);
        }

        .phone-input-group .form-input {
            flex: 1;
        }

        /* Password Field with Eye Icon */
        .password-wrapper {
            position: relative;
        }

        .password-wrapper .form-input {
            padding-right: 50px;
        }

        .eye-button {
            position: absolute;
            right: 16px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            cursor: pointer;
            padding: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.15s ease;
        }

        .eye-button:active {
            transform: translateY(-50%) scale(0.9);
        }

        .eye-button svg {
            width: 22px;
            height: 22px;
            stroke: #9BB0CF;
            stroke-width: 2;
        }

        /* Privacy Agreement */
        .privacy-agreement {
            display: flex;
            align-items: flex-start;
            gap: 10px;
            margin: 20px 0 24px;
        }

        .checkbox-wrapper {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .checkbox-input {
            position: absolute;
            opacity: 0;
            cursor: pointer;
        }

        .checkbox-custom {
            width: 22px;
            height: 22px;
            border-radius: 6px;
            background: linear-gradient(180deg, #071330 0%, #081A38 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: inset 0 4px 12px rgba(3, 7, 18, 0.6);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.15s ease;
            flex-shrink: 0;
        }

        .checkbox-input:checked + .checkbox-custom {
            background: rgba(31, 225, 200, 0.15);
            border-color: #1FE1C8;
            box-shadow: 0 0 12px rgba(31, 225, 200, 0.3), inset 0 2px 8px rgba(31, 225, 200, 0.2);
        }

        .checkbox-custom svg {
            width: 14px;
            height: 14px;
            stroke: #1FE1C8;
            stroke-width: 3;
            opacity: 0;
            transition: opacity 0.15s ease;
        }

        .checkbox-input:checked + .checkbox-custom svg {
            opacity: 1;
        }

        .privacy-text {
            font-size: 13px;
            color: #9BB0CF;
            line-height: 1.5;
            flex: 1;
            padding-top: 2px;
        }

        .privacy-link {
            color: #FF5757;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.15s ease;
        }

        .privacy-link:hover {
            color: #FF6B6B;
        }

        /* Register Button */
        .register-button {
            width: 100%;
            height: 62px;
            border-radius: 34px;
            background: linear-gradient(90deg, #2FF3D3 0%, #18D9BE 100%);
            border: none;
            font-size: 18px;
            font-weight: 700;
            letter-spacing: 4px;
            color: #02171A;
            cursor: pointer;
            transition: all 0.15s ease;
            box-shadow: 0 12px 30px rgba(24, 210, 186, 0.18);
            font-family: 'Poppins', sans-serif;
        }

        .register-button:active {
            transform: scale(0.98);
        }

        .register-button:disabled {
            opacity: 0.4;
            cursor: not-allowed;
            box-shadow: none;
        }

        .register-button:disabled:active {
            transform: none;
        }

        /* Responsive */
        @media (min-width: 768px) {
            body {
                justify-content: center;
                padding: 40px 20px;
            }

            .header {
                margin-bottom: 0;
            }
        }

        @media (max-width: 360px) {
            .card {
                padding: 18px;
            }

            .phone-input-group {
                flex-direction: column;
            }

            .country-code {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <div class="header">
        <div class="back-button">
            <svg viewBox="0 0 24 24" fill="none">
                <path d="M15 18L9 12L15 6" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </div>
        <div class="logo">
            <span class="logo-gradient">Jalwa.Game</span>
        </div>
        <div class="language-selector">
            <svg class="flag-icon" viewBox="0 0 24 24">
                <rect width="24" height="24" rx="3" fill="#B22234"/>
                <rect width="24" height="1.85" fill="white"/>
                <rect y="3.7" width="24" height="1.85" fill="white"/>
                <rect y="7.4" width="24" height="1.85" fill="white"/>
                <rect y="11.1" width="24" height="1.85" fill="white"/>
                <rect y="14.8" width="24" height="1.85" fill="white"/>
                <rect y="18.5" width="24" height="1.85" fill="white"/>
                <rect y="22.2" width="24" height="1.85" fill="white"/>
                <rect width="9.6" height="12.8" fill="#3C3B6E"/>
            </svg>
            <span>EN</span>
        </div>
    </div>

    <!-- Main Container -->
    <div class="container">
        <div class="card">
            <!-- Title Section -->
            <div class="title-section">
                <h1 class="title">Register</h1>
                <p class="subtitle">Please register by phone number or email</p>
                <div class="divider"></div>
            </div>

            <!-- Phone Register Icon -->
            <div class="phone-register">
                <div class="phone-icon">
                    <svg viewBox="0 0 24 24" fill="none">
                        <path d="M22 16.92V19.92C22 20.92 21.21 21.74 20.22 21.92C19.68 21.99 19.12 22.01 18.54 22.01C9.61002 22.01 2.39002 14.79 2.39002 5.86C2.39002 5.28 2.40002 4.72 2.47002 4.18C2.65002 3.19 3.47002 2.4 4.47002 2.4H7.47002C8.35002 2.4 9.09002 3.06 9.17002 3.93C9.24002 4.62 9.35002 5.29 9.51002 5.94C9.73002 6.81 9.46002 7.73 8.82002 8.37L7.21002 9.98C8.76002 13.02 11.99 16.24 15.04 17.8L16.65 16.19C17.29 15.55 18.2 15.28 19.08 15.5C19.73 15.66 20.4 15.77 21.09 15.84C21.97 15.92 22.63 16.67 22.63 17.55" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <div class="phone-register-text">Register your phone</div>
            </div>

            <!-- Form -->
            <form id="registerForm">
                <!-- Phone Number -->
                <div class="form-group">
                    <label class="form-label">Phone number</label>
                    <div class="phone-input-group">
                        <select class="country-code" id="countryCode">
                            <option value="+91">+91</option>
                            <option value="+1">+1</option>
                            <option value="+44">+44</option>
                            <option value="+86">+86</option>
                            <option value="+81">+81</option>
                        </select>
                        <input type="tel" class="form-input" id="phoneNumber" placeholder="Enter phone number" required>
                    </div>
                </div>

                <!-- Set Password -->
                <div class="form-group">
                    <label class="form-label">Set password</label>
                    <div class="password-wrapper">
                        <input type="password" class="form-input" id="password" placeholder="Enter password" required>
                        <button type="button" class="eye-button" id="togglePassword">
                            <svg viewBox="0 0 24 24" fill="none" id="eyeIcon">
                                <path d="M15.58 12C15.58 13.98 13.98 15.58 12 15.58C10.02 15.58 8.42004 13.98 8.42004 12C8.42004 10.02 10.02 8.42 12 8.42C13.98 8.42 15.58 10.02 15.58 12Z" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M12 20.27C15.53 20.27 18.82 18.19 21.11 14.59C22.01 13.18 22.01 10.81 21.11 9.39997C18.82 5.79997 15.53 3.71997 12 3.71997C8.46997 3.71997 5.17997 5.79997 2.88997 9.39997C1.98997 10.81 1.98997 13.18 2.88997 14.59C5.17997 18.19 8.46997 20.27 12 20.27Z" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </button>
                    </div>
                </div>

                <!-- Confirm Password -->
                <div class="form-group">
                    <label class="form-label">Confirm password</label>
                    <div class="password-wrapper">
                        <input type="password" class="form-input" id="confirmPassword" placeholder="Confirm password" required>
                        <button type="button" class="eye-button" id="toggleConfirmPassword">
                            <svg viewBox="0 0 24 24" fill="none" id="eyeIconConfirm">
                                <path d="M15.58 12C15.58 13.98 13.98 15.58 12 15.58C10.02 15.58 8.42004 13.98 8.42004 12C8.42004 10.02 10.02 8.42 12 8.42C13.98 8.42 15.58 10.02 15.58 12Z" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M12 20.27C15.53 20.27 18.82 18.19 21.11 14.59C22.01 13.18 22.01 10.81 21.11 9.39997C18.82 5.79997 15.53 3.71997 12 3.71997C8.46997 3.71997 5.17997 5.79997 2.88997 9.39997C1.98997 10.81 1.98997 13.18 2.88997 14.59C5.17997 18.19 8.46997 20.27 12 20.27Z" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </button>
                    </div>
                </div>

                <!-- Invite Code -->
                <div class="form-group">
                    <label class="form-label">Invite code</label>
                    <input type="text" class="form-input" id="inviteCode" placeholder="Enter invite code (Optional)">
                </div>

                <!-- Privacy Agreement -->
                <div class="privacy-agreement">
                    <label class="checkbox-wrapper">
                        <input type="checkbox" class="checkbox-input" id="privacyCheckbox" required>
                        <div class="checkbox-custom">
                            <svg viewBox="0 0 24 24" fill="none">
                                <path d="M5 13L9 17L19 7" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </label>
                    <div class="privacy-text">
                        I have read and agree <a href="#" class="privacy-link">Privacy Agreement</a>
                    </div>
                </div>

                <!-- Register Button -->
                <button type="submit" class="register-button" id="registerBtn" disabled>
                    REGISTER
                </button>
            </form>
        </div>
    </div>

    <script>
        // Form validation and button state
        const form = document.getElementById('registerForm');
        const phoneNumber = document.getElementById('phoneNumber');
        const password = document.getElementById('password');
        const confirmPassword = document.getElementById('confirmPassword');
        const privacyCheckbox = document.getElementById('privacyCheckbox');
        const registerBtn = document.getElementById('registerBtn');

        // Toggle password visibility
        const togglePassword = document.getElementById('togglePassword');
        const toggleConfirmPassword = document.getElementById('toggleConfirmPassword');
        const eyeIcon = document.getElementById('eyeIcon');
        const eyeIconConfirm = document.getElementById('eyeIconConfirm');

        togglePassword.addEventListener('click', function() {
            const type = password.type === 'password' ? 'text' : 'password';
            password.type = type;
            
            if (type === 'text') {
                eyeIcon.innerHTML = `
                    <path d="M14.53 9.47004L9.47004 14.53C8.82004 13.88 8.42004 12.99 8.42004 12C8.42004 10.02 10.02 8.42004 12 8.42004C12.99 8.42004 13.88 8.82004 14.53 9.47004Z" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M17.82 5.76998C16.07 4.44998 14.07 3.72998 12 3.72998C8.46997 3.72998 5.17997 5.80998 2.88997 9.40998C1.98997 10.82 1.98997 13.19 2.88997 14.6C3.67997 15.84 4.59997 16.91 5.59997 17.77" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M8.42004 19.5301C9.56004 20.0101 10.77 20.2701 12 20.2701C15.53 20.2701 18.82 18.1901 21.11 14.5901C22.01 13.1801 22.01 10.8101 21.11 9.40005C20.78 8.88005 20.42 8.39005 20.05 7.93005" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M15.5099 12.7C15.2499 14.11 14.0999 15.26 12.6899 15.52" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M9.47 14.53L2 22" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M22 2L14.53 9.47" stroke-linecap="round" stroke-linejoin="round"/>
                `;
            } else {
                eyeIcon.innerHTML = `
                    <path d="M15.58 12C15.58 13.98 13.98 15.58 12 15.58C10.02 15.58 8.42004 13.98 8.42004 12C8.42004 10.02 10.02 8.42 12 8.42C13.98 8.42 15.58 10.02 15.58 12Z" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M12 20.27C15.53 20.27 18.82 18.19 21.11 14.59C22.01 13.18 22.01 10.81 21.11 9.39997C18.82 5.79997 15.53 3.71997 12 3.71997C8.46997 3.71997 5.17997 5.79997 2.88997 9.39997C1.98997 10.81 1.98997 13.18 2.88997 14.59C5.17997 18.19 8.46997 20.27 12 20.27Z" stroke-linecap="round" stroke-linejoin="round"/>
                `;
            }
        });

        toggleConfirmPassword.addEventListener('click', function() {
            const type = confirmPassword.type === 'password' ? 'text' : 'password';
            confirmPassword.type = type;
            
            if (type === 'text') {
                eyeIconConfirm.innerHTML = `
                    <path d="M14.53 9.47004L9.47004 14.53C8.82004 13.88 8.42004 12.99 8.42004 12C8.42004 10.02 10.02 8.42004 12 8.42004C12.99 8.42004 13.88 8.82004 14.53 9.47004Z" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M17.82 5.76998C16.07 4.44998 14.07 3.72998 12 3.72998C8.46997 3.72998 5.17997 5.80998 2.88997 9.40998C1.98997 10.82 1.98997 13.19 2.88997 14.6C3.67997 15.84 4.59997 16.91 5.59997 17.77" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M8.42004 19.5301C9.56004 20.0101 10.77 20.2701 12 20.2701C15.53 20.2701 18.82 18.1901 21.11 14.5901C22.01 13.1801 22.01 10.8101 21.11 9.40005C20.78 8.88005 20.42 8.39005 20.05 7.93005" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M15.5099 12.7C15.2499 14.11 14.0999 15.26 12.6899 15.52" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M9.47 14.53L2 22" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M22 2L14.53 9.47" stroke-linecap="round" stroke-linejoin="round"/>
                `;
            } else {
                eyeIconConfirm.innerHTML = `
                    <path d="M15.58 12C15.58 13.98 13.98 15.58 12 15.58C10.02 15.58 8.42004 13.98 8.42004 12C8.42004 10.02 10.02 8.42 12 8.42C13.98 8.42 15.58 10.02 15.58 12Z" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M12 20.27C15.53 20.27 18.82 18.19 21.11 14.59C22.01 13.18 22.01 10.81 21.11 9.39997C18.82 5.79997 15.53 3.71997 12 3.71997C8.46997 3.71997 5.17997 5.79997 2.88997 9.39997C1.98997 10.81 1.98997 13.18 2.88997 14.59C5.17997 18.19 8.46997 20.27 12 20.27Z" stroke-linecap="round" stroke-linejoin="round"/>
                `;
            }
        });

        // Validate form and enable/disable button
        function validateForm() {
            const phoneValid = phoneNumber.value.trim().length > 0;
            const passwordValid = password.value.trim().length > 0;
            const confirmPasswordValid = confirmPassword.value.trim().length > 0;
            const passwordsMatch = password.value === confirmPassword.value;
            const privacyChecked = privacyCheckbox.checked;

            registerBtn.disabled = !(phoneValid && passwordValid && confirmPasswordValid && passwordsMatch && privacyChecked);
        }

        phoneNumber.addEventListener('input', validateForm);
        password.addEventListener('input', validateForm);
        confirmPassword.addEventListener('input', validateForm);
        privacyCheckbox.addEventListener('change', validateForm);

        // Form submission
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            if (!registerBtn.disabled) {
                // Add submission logic here
                console.log('Form submitted:', {
                    countryCode: document.getElementById('countryCode').value,
                    phone: phoneNumber.value,
                    password: password.value,
                    inviteCode: document.getElementById('inviteCode').value
                });
                
                alert('Registration submitted successfully!');
            }
        });

        // Back button
        document.querySelector('.back-button').addEventListener('click', function() {
            window.history.back();
        });
    </script>
</body>
</html>
