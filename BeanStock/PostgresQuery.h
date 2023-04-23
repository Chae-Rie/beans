#pragma once
#include "QueryInterface.h"

class PostgresQuery : public QueryInterface {
public: //--- Konstruktion/ Destruktion
	PostgresQuery();
	virtual ~PostgresQuery();


	virtual void AddNewEntry()override;
	virtual void DeleteEntry()override;
	virtual void GetNewestEntry()override;
	virtual void SubscribeChannel(const char* channel)override;
	virtual void UnsubscribeChannel(const char* channel)override;
private:

};

