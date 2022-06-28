const initialState = {
    posts: {
        results: [],
        count: 0,
        next: null,
        previous: null,
    },
    user: {
        user_name : "",
        email : "", 
        token : "",
        token_expires_at : "",
    }
};

export default initialState;
