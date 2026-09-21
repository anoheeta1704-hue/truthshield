import { Outlet, NavLink } from 'react-router-dom'
import { Shield, Upload, Radio, Clock, BarChart3 } from 'lucide-react'

const navItems = [
  { to: '/upload', label: 'Upload', icon: Upload },
  { to: '/live', label: 'Live', icon: Radio },
  { to: '/history', label: 'History', icon: Clock },
  { to: '/dashboard', label: 'Dashboard', icon: BarChart3 },
]

function Layout() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <header className="sticky top-0 z-50 border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="container mx-auto flex h-14 items-center justify-between px-4">
          <NavLink to="/" className="flex items-center gap-2">
            <Shield className="h-6 w-6" />
            <span className="text-lg font-semibold tracking-tight">TruthShield</span>
          </NavLink>
          <nav className="flex items-center gap-1">
            {navItems.map((item) => {
              const Icon = item.icon
              return (
              <NavLink
                key={item.to}
                to={item.to}
                className={({ isActive }) =>
                  `flex items-center gap-1.5 rounded-lg px-3 py-2 text-sm font-medium transition-colors ${
                    isActive
                      ? 'bg-muted text-foreground'
                      : 'text-muted-foreground hover:bg-muted/50 hover:text-foreground'
                  }`
                }
              >
                <Icon className="h-4 w-4" />
                {item.label}
              </NavLink>
            )})}
          </nav>
        </div>
      </header>
      <main className="container mx-auto px-4 py-8">
        <Outlet />
      </main>
    </div>
  )
}

export default Layout
