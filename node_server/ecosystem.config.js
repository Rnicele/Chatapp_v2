module.exports = {
  apps: [
    {
      name: "Node Socket Server",
      script: "index.js",
      watch: true,
      env: {
        NODE_ENV: "development",
      },
    },
  ],
};
