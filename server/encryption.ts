import * as crypto from 'crypto'

const authTagLength = 16
const algo = 'aes-256-ccm'

export function cipher(value: string): string {
  const config = useRuntimeConfig()
  const IV = crypto.randomBytes(13)
  const cipher = crypto.createCipheriv(
    algo,
    Buffer.from(config.aesEncryptionKey, 'base64url'),
    IV,
    { authTagLength }
  )

  const res = cipher.update(value, 'utf-8', 'base64url') + cipher.final('base64url')
  const authTag = cipher.getAuthTag().toString('base64url')

  return `${res}:${authTag}:${IV.toString('base64url')}`
}

export function decipher(value: string): string {
  const config = useRuntimeConfig()
  const [cipherValue, authTag, IV] = value.split(':')

  const decipher = crypto.createDecipheriv(
    algo,
    Buffer.from(config.aesEncryptionKey, 'base64url'),
    Buffer.from(IV, 'base64url'),
    { authTagLength }
  )

  decipher.setAuthTag(Buffer.from(authTag, 'base64url'))

  return decipher.update(cipherValue, 'base64url').toString('utf-8') + decipher.final('utf-8')
}
