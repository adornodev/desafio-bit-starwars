db.createUser({
  user: "bitsw",
  pwd: "bitsw123",
  roles: [
    {
      role: "readWrite",
      db: "BitSW"
    }
  ]
});

db.createCollection("planets");
