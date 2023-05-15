#pragma once

#include <libpq-fe.h>
#include </dev/vcpkg/packages/libpq_x64-windows/include/server/catalog/pg_type_d.h> 

class QueryInterface {
public:
	virtual void AddNewEntry() = 0;
	virtual void DeleteEntry() = 0;
	virtual void GetNewestEntry() = 0;
	virtual void SubscribeChannel(const char* channel) = 0;
	virtual void UnsubscribeChannel(const char* channel) = 0;


private:

};

