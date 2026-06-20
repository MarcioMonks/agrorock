export default function Home() {
  return (
    <main className="min-h-screen bg-zinc-950 text-zinc-100">
      <section className="mx-auto flex min-h-screen max-w-5xl flex-col justify-center px-6 py-16">
        <p className="mb-4 text-sm font-semibold uppercase tracking-[0.3em] text-emerald-400">
          AgroRock
        </p>

        <h1 className="max-w-3xl text-4xl font-bold tracking-tight sm:text-6xl">
          Sistema de apoio à Engenharia Agronômica
        </h1>

        <p className="mt-6 max-w-2xl text-lg leading-8 text-zinc-300">
          O AgroRock organiza dados, cálculos e informações de campo para ajudar
          o agrônomo a decidir melhor.
        </p>

        <div className="mt-10 rounded-2xl border border-zinc-800 bg-zinc-900/70 p-6">
          <h2 className="text-xl font-semibold">Módulos iniciais</h2>

          <ul className="mt-4 space-y-3 text-zinc-300">
            <li>• Calculadoras agronômicas</li>
            <li>• Diário técnico</li>
            <li>• Propriedades e talhões</li>
            <li>• Relatórios</li>
          </ul>
        </div>

        <p className="mt-10 text-sm text-zinc-500">
          Primeiro entender. Depois codar. Depois integrar.
        </p>
      </section>
    </main>
  );
}