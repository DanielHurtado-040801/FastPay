import { useNavigate } from "react-router-dom";

export function UsuariosCard({ usuario }) {
  const navigate = useNavigate();

  return (
    <div className="max-w-52 p-6 lg:max-h-60 lg:mt-0 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 mt-5">
      <a href="#">
        <h5 className="mb-1 text-2xl font-bold tracking-tight text-blue-600 dark:text-white">
          {usuario.username}
        </h5>
      </a>
      <p className="mb-1 font-normal text-gray-700 dark:text-gray-400">
        {usuario.name} {usuario.last_name}
      </p>
      <p className="mb-1 font-normal text-gray-700 dark:text-gray-400">
        {usuario.email}
      </p>
      <a
        href={`/usuarios/${usuario.id}`}
        className="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
      >
        Edit
        <svg
          aria-hidden="true"
          className="w-4 h-4 ml-2 -mr-1"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fillRule="evenodd"
            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
            clipRule="evenodd"
          ></path>
        </svg>
      </a>
    </div>
  );
}
