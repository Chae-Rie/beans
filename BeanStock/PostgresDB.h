#pragma once
#include "DatabaseInterface.h"
class PostgresDB : public DatabaseInterface {
public: //--- Konstruktion/ Destruktion
	PostgresDB();
	virtual ~PostgresDB();

	std::shared_ptr<PGconn> ConnectDatabase() override;
	BOOL DisconnectDatabase() override;

private:

};



