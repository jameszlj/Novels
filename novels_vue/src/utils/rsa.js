import { JSEncrypt } from 'jsencrypt'

export function rsaEncrypt(data) {
  const publicKey = `MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDkm92CXjfCVsQPnuVHpzQFPUWP
  LOz7EPhfvv3pDGDec5xLZUtU1qWwa0tJnyTEzpcBYCxtZZ+1S5f/rfKuxbcw077J
  ZEuatbdSO+QCxYm5Q+AUJ9fbR79m7MEsXeo5LPV22RXMOJeM9/7MwwotFolBlIQu
  rgrR5fORA06KWbZCMwIDAQAB`
  const jse = new JSEncrypt()
  jse.setPublicKey(publicKey)
  const result = jse.encrypt(data)
  // console.log("rsa data===>",result)

  return result
}