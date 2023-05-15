
// BeanStock.h : main header file for the PROJECT_NAME application
//

#pragma once

#ifndef __AFXWIN_H__
	#error "include 'pch.h' before including this file for PCH"
#endif

#include "resource.h"		// main symbols


// CBeanStockApp:
// See BeanStock.cpp for the implementation of this class                                                                                  
//

class CBeanStockApp : public CWinApp
{
public:
	CBeanStockApp();

// Overrides
public:
	virtual BOOL InitInstance();

// Implementation

	DECLARE_MESSAGE_MAP()
};

extern CBeanStockApp theApp;
