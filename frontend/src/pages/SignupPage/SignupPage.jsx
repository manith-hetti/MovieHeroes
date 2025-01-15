import { useState } from "react";
import { useNavigate } from "react-router-dom";
import handleErrors from "../HandleErrors";
import { signup } from "../../services/authentication";
// import NavBarLogin from "../../Components/NavBarLogin/NavBarLogin"
import { Link } from 'react-router-dom';
import "./SignupPage.css";
import Navbar from "../../Components/Navbar";
import BackdropSlider from "../../Components/BackdropSlider/BackdropSlider"; // Import the BackdropSlider component

const SignupPage = () => {
const [fullName, setFullName] = useState("");
const [email, setEmail] = useState("");
const [password, setPassword] = useState("");
const [userErrors, setUserErrors] = useState({})
const [isFocused, setIsFocused] = useState(false);
const [resp, setResp] = useState("")
const navigate = useNavigate();

    const handleFullNameChange = (event) => {
        setFullName(event.target.value);
    };
    const handlePasswordChange = (event) => {
        setPassword(event.target.value)
    }

    const handleEmailChange = (event) => {
        setEmail(event.target.value);
    };

    const handleBlur = () => {
        setIsFocused(false);
        const errors = handleErrors(password, email)
        setUserErrors(()=>errors)
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        console.log("Form submitted");
        try {
            const response = await signup(fullName, email, password);
            if(typeof(response) === "string"){
                setResp(response)
            }else{
            console.log("redirecting...:");
                setResp("")
            navigate("/login");
            }
        } catch (err) {
            console.error(err);
            navigate("/signup");
        }
    }

    return (
        <>
        <Navbar />
        <BackdropSlider /> {/* Render the BackdropSlider component */}
        <div className="signup-container">
            <div className="signup-content">
                <h2>Sign Up for Your Free Account!</h2>
                <form onSubmit={handleSubmit} className="signup-form">
                    <label htmlFor="fullName">Full Name:</label>
                    <input
                        placeholder="Enter your full name..."
                        id="fullName"
                        type="text"
                        value={fullName}
                        onChange={handleFullNameChange}
                    />
                    <label htmlFor="email">Email:</label>
                    <input
                        placeholder="user@email.com"
                        id="email"
                        type="email"
                        value={email}
                        onChange={handleEmailChange}
                        onFocus={()=>setIsFocused(true)}
                        onBlur={handleBlur}
                    />
                    <div className="error-message">
                        {resp? <p>{resp}</p>:null}
                        {userErrors.email_errors && userErrors.email_errors.length > 0 && !isFocused && (
                            <div>
                                {userErrors.email_errors.map((error, index) => (
                                    <p key={index}>{error}</p>
                                ))}
                            </div>
                        )}
                    </div>
                    <label htmlFor="password">Password:</label>
                    <input
                        placeholder="Password"
                        id="password"
                        type="password"
                        value={password}
                        onChange={handlePasswordChange}
                        onFocus={()=>setIsFocused(true)}
                        onBlur={handleBlur}
                    />
                    <div className="error-message">
                        {userErrors.pwd_errors && userErrors.pwd_errors.length > 0 && !isFocused && (
                            <div>
                                {userErrors.pwd_errors.map((error, index) => (
                                    <p key={index}>{error}</p>
                                ))}
                            </div>
                        )}
                    </div>
                    <input role="submit-button" id="submit" type="submit" value="Submit" className="submit_btn"/>
                </form>
                <div className="login-redirect">
                    <p>If you already have an account</p>
                    <Link to="/login">Login</Link>
                </div>
            </div>
        </div>
        </>
    )
}

export default SignupPage
