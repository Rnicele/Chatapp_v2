const server = require("http").createServer();
const { Server } = require("socket.io");
const io = new Server(server, {
  cors: {
    origin: function (origin, fn) {
      return fn(null, origin);
    },
    credentials: true,
  },
  allowEIO3: true,
});

io.on("connection", (socket) => {
  socket.on("joinRoom", (room) => {
    socket.rooms.forEach((joinedRoom) => {
      if (Number.isInteger(joinedRoom)) {
        socket.emit("test", `LEAVING ${joinedRoom}`);
        socket.leave(joinedRoom);
      }
    });
    socket.join(room);
  });
  socket.on("sendMessage", ({ room, message }) =>
    socket.broadcast.to(room).emit("newMessage", message)
  );
});

server.listen(3000, () => {
  console.log("listening on *:3000");
});
