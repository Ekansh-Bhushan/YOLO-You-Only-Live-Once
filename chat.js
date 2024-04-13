import { createServer } from "http";
import express from "express";
import { Server } from "socket.io";
import cors from "cors";
import path from "path";
import { fileURLToPath } from "url";

// Assuming you have an AI model imported and set up for generating responses
import { generateResponse } from "./yourAIModel.js";

const app = express();
app.use(cors());

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const publicPath = path.join(__dirname, "public");
const httpServer = createServer(app);

app.use(express.static(publicPath));

const PORT = process.env.PORT || 5500;
const io = new Server(httpServer, {
  path: "/socket.io",
  cors: {
    origin: "*", // Allow all origins
    methods: ["GET", "POST"], // Allow GET and POST methods
  },
});

io.on("connection", (socket) => {
  console.log(`User ${socket.id} connected`);

  socket.on("message", async (textmsg) => {
    console.log(textmsg);
    
    // Generate AI response
    const aiResponse = await generateResponse(textmsg);

    // Send response to all connected clients
    io.emit("message", aiResponse);
  });
});

// write a get api endpoint
app.get("/", (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

httpServer.listen(PORT, () => console.log(`listening on port ${PORT}`));
