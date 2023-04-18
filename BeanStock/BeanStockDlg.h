
// BeanStockDlg.h : header file
//

#pragma once


// CBeanStockDlg dialog
class CBeanStockDlg : public CDialogEx
{
// Construction
public:
	CBeanStockDlg(CWnd* pParent = nullptr);	// standard constructor

// Dialog Data
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_BEANSTOCK_DIALOG };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support


// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()
private:
	CString GetEditInput(UINT uiRessourceId);
public:
	afx_msg void OnDTNChangeDtPickerPurchase(NMHDR* pNMHDR, LRESULT* pResult);
};
