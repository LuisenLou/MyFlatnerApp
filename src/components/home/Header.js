import { NavLink} from 'react-router-dom';
import { Typewriter } from 'react-simple-typewriter'


function Header(){

    return(
      <div className="relative isolate pt-14 lg:px-8">
        <div className="absolute inset-x-0 -top-20 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80" aria-hidden="true">
          <div className="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#2ECC71] to-[#2ECC71] opacity-20 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]" style={{clipPath: "polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)" }}>
          </div>
        </div>
        <div className="mx-auto max-w-4xl items-center sm:py-10 lg:py-2 px-5">
          <div className="hidden sm:mb-8 sm:flex sm:justify-center">
            <h2 className="text-3xl font-bold text-center tracking-tight text-gray-900 sm:text-5xl">
               ¿Buscas compañero de piso, habitación o piso para compartir?</h2>
          </div>
          <div className="text-center pb-20">
            <h1 className="text-4xl font-bold tracking-tight text-gray-700 pb-10 sm:text-7xl "> Búsqueda :
              <div className="mb-5"></div>
              <div style={{color:'#2ECC71', fontWeight:'bold'}}>
                <Typewriter
                  words={['Rápida', 'Fácil', 'Segura', ' Flatner']} 
                  loop={0}
                  cursor
                  cursorStyle='_'
                  cursorColor='black'
                  typeSpeed={40}
                  deleteSpeed={40}
                  delaySpeed={1500}
                />
              </div>
            </h1>
            <p className="mt-8 text-lg leading-8 text-gray-600"> Búsqueda de habitaciones, compañeros de piso y control de incidencias del propietario con FLATNER</p>
            <div className="mt-14 flex items-center justify-center gap-x-6">
              <button href="#" className="rounded-md bg-emerald-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-emerald-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-emerald-600"> Instalar App</button>
              <NavLink to="/nosotros" className="text-sm font-semibold leading-6 text-gray-900">Saber mas <span aria-hidden="true">→</span></NavLink>
            </div>
          </div>
        </div>
        <div className="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]" aria-hidden="true">
          <div className="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 bg-gradient-to-tr from-[#2ECC71] to-[#2ECC71] opacity-20 sm:left-[calc(50%+36rem)] sm:w-[72.1875rem]" style={{clipPath: "polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)"}}>
          </div>
        </div>
      </div>
    )
}

export default Header;