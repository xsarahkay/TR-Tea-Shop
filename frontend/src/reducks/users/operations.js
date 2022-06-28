import API from "../../API"
import { signInAction,signUpAction,signOutAction } from "./actions"
import {push} from "connected-react-router"

const api = new API ()
const LOGIN_USER_KEY = "LOGIN_USER_KEY"

export const fetchUserFromLocalStorage = () => {
    return async (dispatch) => {
        const userJSON= localStorage.getItem (LOGIN_USER_KEY)
        if (userJSON && userJSON.token !== "") {
            dispatch(signInAction(JSON.parse(userJSON)))
        }
    }

}

export const signUp = (user_name, email, password) => {
    return async (dispatch) => {
         if (user_name==="" || email==="" || password ==="" ) {
             alert ("Please fill out name, email, password")
             return false
         }

         return api.signUp (username, email, password)
    }
}