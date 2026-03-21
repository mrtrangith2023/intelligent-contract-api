import { GenLayerClient } from "genlayer-js";

const client = new GenLayerClient({
  apiUrl: "http://127.0.0.1:8000/api", // backend URL
});

export default client;