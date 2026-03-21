import { GenLayerClient } from "genlayer-js";

const client = new GenLayerClient({
  apiUrl: "http://192.168.56.1:8000/api", // backend IP + port
});

export default client;