import { decipher } from '~/server/encryption'
import { VERSION } from '~/server/common'

export default defineEventHandler((event) => {
  const q = useQuery(event)

  const startCursor = q.start
  const token = (q.token || getCookie(event, 'nct-v1')) as string

  if (!token) {
    return createError({ statusCode: 401, statusMessage: 'Unauthorized', message: 'Missing token' })
  }

  return $fetch('https://api.notion.com/v1/search', {
    method: 'POST',
    body: {
      sort: {
        direction: 'descending',
        timestamp: 'last_edited_time',
      },
      filter: { value: 'database', property: 'object' },
      ...(startCursor ? { start_cursor: startCursor } : {}),
      page_size: 100,
    },
    headers: {
      ...VERSION,
      Authorization: `Bearer ${decipher(token)}`,
    },
  }).catch((error) => {
    // eslint-disable-next-line no-console
    console.error(error)
    throw new Error('An error occurred while converting code in access-token.')
  })
})
