#include "pch.h"
#include "PostgresDB.h"

PostgresDB::PostgresDB() {
}

PostgresDB::~PostgresDB() {
}

std::shared_ptr<PGconn> PostgresDB::ConnectDatabase() {
	return std::shared_ptr<PGconn>();
}

BOOL PostgresDB::DisconnectDatabase() {
	return 0;
}
