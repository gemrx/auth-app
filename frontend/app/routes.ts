import { type RouteConfig, index, route } from "@react-router/dev/routes";

export default [
  index("routes/login.tsx"),
  route("signup", "routes/signup.tsx"),
  route("welcome/:name", "routes/welcome.tsx")
] satisfies RouteConfig;
