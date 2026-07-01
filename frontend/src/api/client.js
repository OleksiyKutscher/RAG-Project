import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const queryDocs = async (question, k = 4) => {
  const response = await api.post("/query", { question, k });
  return response.data;
};