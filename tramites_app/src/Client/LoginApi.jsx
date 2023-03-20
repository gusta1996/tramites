import {BASE_API} from '../utils/constants.jsx'

export async function LoginApi(formData){
    try{
        const url=`${BASE_API}/login/`
        const params= {
            method:"POST",
            headers:{
                "Content-type":"application/json",
            },
            body:JSON.stringify(formData),
        };

        const response=await fetch(url,params);
        if (response.status!==200){
            throw new Error("Usuario y contraseña incorrecta")
        }

        const result=await response.json()
        return result

    }catch (error) {
        throw error
    }
}

export async function getMeApi(token) {
    try{
        const url=`${BASE_API}/api/auth/me/`;
        const params={
            headers:{
                Authorization:`Bearer ${token}`
            }
        }
        const response =await fetch(url,params)
        const result = await response.json();
        return result;
    }
    catch (e) {
        throw e;

    }
}