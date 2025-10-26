import axios from "axios";

const BASE_URL = "http://localhost:8000/accounts"; // FastAPI backend

export const createAccount = async (accountData) => {
  try {
    const response = await axios.post(BASE_URL + "/", accountData);
    return response.data;
  } catch (error) {
    if (error.response) {
      throw new Error(error.response.data.detail);
    } else {
      throw new Error("Network Error");
    }
  }
};
