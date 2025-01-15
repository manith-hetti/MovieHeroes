const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

export const updateAvatar = async (token=null, avatar) => {
    console.log("Updating avatar");
    const payload = {
        token: token,
        avatar:avatar

    };

    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(payload),
    };

    let response = await fetch(`${BACKEND_URL}/userProfile`, requestOptions);


    const data = await response.json()

    // console.log("this is the avatar response", data.update_user.avatar)

    if (response.status !== 200) {
    throw new Error("Unable to an avatar");
    } else {
    return data.update_user.avatar; //we may need to update this to access a specific item
    }
};

export async function getAvatarByUserById(token) {
    console.log("Token:", token);
    const requestOptions = {
        method: "GET",
        headers: {
            Authorization: `Bearer ${token}`,
        },
    };
    console.log("Headers:", requestOptions.headers);
    console.log("Current timestamp: ", Math.floor(Date.now() / 1000));

    let response = await fetch(`${BACKEND_URL}/userProfile`, requestOptions);
    console.log(response.status);

    if (response.status !== 200) {
        throw new Error("Failed to fetch avatar");
    }

    const data = await response.json();
    return data.updated_user.avatar;
}
