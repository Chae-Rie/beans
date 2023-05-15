#pragma once
// Um CompilerFehler vorzubeugen muss in jeder Interfaceklasse die jeweilige libpq-lib hinzügefügt werden

#include <libpq-fe.h>
#include </dev/vcpkg/packages/libpq_x64-windows/include/server/catalog/pg_type_d.h> 

class DatabaseInterface {
public:
	virtual std::shared_ptr<PGconn> ConnectDatabase(const char* connectionstring) = 0;
	virtual BOOL DisconnectDatabase() = 0;

private:

};


