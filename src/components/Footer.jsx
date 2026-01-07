import { useTheme } from '../theme/ThemeProvider'

export default function Footer() {
  const { darkMode } = useTheme()
  const currentYear = new Date().getFullYear()

  return (
    <footer
      className={`mt-auto py-6 border-t ${
        darkMode
          ? 'bg-slate-900 border-slate-800 text-slate-400'
          : 'bg-white border-slate-200 text-slate-600'
      }`}
    >
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="text-sm">
            <p>
              © {currentYear} Sistema de Cotação de Planos de Saúde. Todos os
              direitos reservados.
            </p>
          </div>

          <div className="flex gap-6 text-sm">
            <a
              href="#"
              className={`hover:underline ${
                darkMode ? 'hover:text-slate-200' : 'hover:text-slate-900'
              }`}
            >
              Política de Privacidade
            </a>
            <a
              href="#"
              className={`hover:underline ${
                darkMode ? 'hover:text-slate-200' : 'hover:text-slate-900'
              }`}
            >
              Termos de Uso
            </a>
            <a
              href="#"
              className={`hover:underline ${
                darkMode ? 'hover:text-slate-200' : 'hover:text-slate-900'
              }`}
            >
              Contato
            </a>
          </div>
        </div>

        <div
          className={`text-center text-xs mt-4 pt-4 border-t ${
            darkMode ? 'border-slate-800' : 'border-slate-200'
          }`}
        >
          <p>Desenvolvido com ❤️ usando FastAPI + React + PostgreSQL</p>
        </div>
      </div>
    </footer>
  )
}
