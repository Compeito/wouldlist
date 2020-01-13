export interface Jwt {
  name: string,
  picture: string,
  iss: string,
  aud: string,
  auth_time: number,
  user_id: string,
  sub: string,
  iat: number,
  exp: number,
  firebase: {
    identities: Map<string, Array<string>>,
    sign_in_provider: string,
  }
}
