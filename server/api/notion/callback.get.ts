import { cipher } from '~~/server/encryption'

export default defineEventHandler((event) => {
  const config = useRuntimeConfig()
  const q = useQuery(event)

  if (!q.code) {
    return createError({ statusCode: 401, statusMessage: 'Unauthorized', message: 'Missing code' })
  }

  return $fetch('https://api.notion.com/v1/oauth/token', {
    method: 'POST',
    body: {
      grant_type: 'authorization_code',
      code: q.code,
    },
    headers: {
      Authorization:
        'Basic ' +
        Buffer.from(`${config.public.notionClientId}:${config.notionClientSecret}`).toString(
          'base64'
        ),
    },
  })
    .then((value: any) => {
      const token = cipher(value.access_token)
      setCookie(event, 'nct-v1', token)
      sendRedirect(event, '/new', 302)
      return { token }
    })
    .catch((error) => {
      // eslint-disable-next-line no-console
      console.error(error)
      throw new Error('An error occurred while converting code in access-token.')
    })
  // TODO: set cookie to display infos in frontend
  // TODO: allow creation of private and public links
})

// const dd = {
//   access_token: '',
//   token_type: 'bearer',
//   bot_id: '',
//   workspace_name: 'Arnaud',
//   workspace_icon: '👽',
//   workspace_id: '8e037',
//   owner: {
//     type: 'user',
//     user: {
//       object: 'user',
//       id: '8495e6cc',
//     },
//   },
// }
