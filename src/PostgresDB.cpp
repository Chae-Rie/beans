#include "pch.h"
#include "PostgresDB.h"

PostgresDB::PostgresDB() {
}

PostgresDB::~PostgresDB() {
}

std::shared_ptr<PGconn> PostgresDB::ConnectDatabase(const char* connectionstring) {
	std::shared_ptr<PGconn> m_MainDbConnection(PQconnectdb(connectionstring), PQfinish);

	if( PQstatus(m_MainDbConnection.get()) != CONNECTION_OK ) {
		// something went wrong
		return NULL;
	}

	return m_MainDbConnection;
}

BOOL PostgresDB::DisconnectDatabase() {
	return 0;
}
