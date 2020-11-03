import requests

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'cookie': 'cna=w3bMFomrVBECAW/QcJ3pGn5i; UM_distinctid=17135109e2957e-046c50dc2cd642-34564a78-1fa400-17135109e2be56; mobileSendTime=-1; credibleMobileSendTime=-1; ctuMobileSendTime=-1; riskMobileBankSendTime=-1; riskMobileAccoutSendTime=-1; riskMobileCreditSendTime=-1; riskCredibleMobileSendTime=-1; riskOriginalAccountMobileSendTime=-1; iw.userid="K1iSL19gs+tmXDTXqq1Bmw=="; alipay="K1iSL19gs+tmXDTXqq1Bm0TqCBb8U+LG3Tq0+iJGsA=="; csrfToken=3Q2-FesZ86-EIBe3SG8srXMy; ctoken=dUE314V20m9j6Z4z; LoginForm=alipay_login_home; CLUB_ALIPAY_COM=2088622198125507; ali_apache_tracktmp="uid=2088622198125507"; session.cookieNameId=ALIPAYJSESSIONID; unicard1.vm="K1iSL19gs+tmXDTXqq1Bmw=="; zone=GZ00C; ALIPAYJSESSIONID=RZ41EXffWp0Q8yToT2Hfm48Kw5BFhoauthRZ55GZ00; spanner=ldQs04UPoRff8rKDhs69LDRxR0wqM3+f4EJoL7C0n0A=; rtk=YKb+EdswYjhF72sEkKD3wkV3qzvPqAfemvb0UE9VqPxBqTLwWCz; NEW_ALIPAY_TIP=1',
    'cookie': 'cna=w3bMFomrVBECAW/QcJ3pGn5i; UM_distinctid=17135109e2957e-046c50dc2cd642-34564a78-1fa400-17135109e2be56; mobileSendTime=-1; credibleMobileSendTime=-1; ctuMobileSendTime=-1; riskMobileBankSendTime=-1; riskMobileAccoutSendTime=-1; riskMobileCreditSendTime=-1; riskCredibleMobileSendTime=-1; riskOriginalAccountMobileSendTime=-1; csrfToken=3Q2-FesZ86-EIBe3SG8srXMy; session.cookieNameId=ALIPAYJSESSIONID; unicard1.vm="K1iSL19gs+tmXDTXqq1Bmw=="; spanner=ldQs04UPoRff8rKDhs69LDRxR0wqM3+f4EJoL7C0n0A=; NEW_ALIPAY_TIP=1; ctoken=RZlCIP56ZnKTjwsU; LoginForm=alipay_login_auth; alipay="K1iSL19gs+tmXDTXqq1Bm0TqCBb8U+LG3Tq0+iJGsA=="; CLUB_ALIPAY_COM=2088622198125507; iw.userid="K1iSL19gs+tmXDTXqq1Bmw=="; ali_apache_tracktmp="uid=2088622198125507"; ALIPAYJSESSIONID=RZ41RbFa3jNzn7D0aUJ6sWakxibsoJauthRZ55GZ00; zone=GZ00C; rtk=qJYVmwgdIKtvmWgNoJncdobsXbFIYTZy7FBQAY4L2IaWYJjd26t',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3742.400 QQBrowser/10.5.3864.400',
}

sessions = requests.Session()
html = sessions.get(url="https://consumeprod.alipay.com/record/standard.htm", headers=header)
print(html.text)





