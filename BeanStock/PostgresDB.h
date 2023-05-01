#pragma once
#include "DatabaseInterface.h"
class PostgresDB : public DatabaseInterface {
public: //--- Konstruktion/ Destruktion
	PostgresDB();
	virtual ~PostgresDB();

	std::shared_ptr<PGconn> ConnectDatabase(const char* connectionstring) override;
	BOOL DisconnectDatabase() override;

private:
	std::shared_ptr<PGconn> m_MainDbConnection;
	PGresult* m_pgresult;
};



