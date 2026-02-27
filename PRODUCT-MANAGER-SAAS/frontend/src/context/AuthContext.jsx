import { createContext, useMemo, useState } from "react";

export const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [token, setToken] = useState(localStorage.getItem("token"));

  const value = useMemo(() => ({
    token,
    isAuthenticated: Boolean(token),
    login: (newToken) => {
      localStorage.setItem("token", newToken);
      setToken(newToken);
    },
    logout: () => {
      localStorage.removeItem("token");
      setToken(null);
    },
  }), [token]);

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
