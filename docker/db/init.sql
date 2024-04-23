CREATE TABLE "servers" (
  "name" text NOT NULL,
  "address" inet NOT NULL
);

ALTER TABLE "servers"
ADD CONSTRAINT "servers_name" PRIMARY KEY ("name");

CREATE TABLE "latencies" (
  "server_name" text NOT NULL,
  "time" timestamp NOT NULL,
  "latency" double precision NOT NULL
);

ALTER TABLE "latencies"
ADD CONSTRAINT "latencies_server_name_time" PRIMARY KEY ("server_name", "time");

ALTER TABLE "latencies"
ADD FOREIGN KEY ("server_name") REFERENCES "servers" ("name")