import { useEffect, useState } from "react";
import api from "./services/api";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function App() {
  const [skills, setSkills] = useState([]);
  const [jobs, setJobs] = useState([]);
  const [roles, setRoles] = useState([]);
  const [selectedRole, setSelectedRole] = useState("");

  useEffect(() => {
    api
      .get("/skills")
      .then((response) => {
        const filteredSkills = response.data.filter(
          (skill) => skill.Count > 0
        );
        setSkills(filteredSkills);
      })
      .catch(console.error);

    api
      .get("/jobs")
      .then((response) => {
        setJobs(response.data);
      })
      .catch(console.error);

    api
      .get("/roles")
      .then((response) => {
        setRoles(response.data);
      })
      .catch(console.error);
  }, []);

  const filteredJobs =
    selectedRole === ""
      ? jobs
      : jobs.filter((job) => job.role === selectedRole);

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-100 to-blue-100">

      {/* Header */}
      <div className="bg-blue-700 text-white shadow-lg">
        <div className="max-w-7xl mx-auto py-8 px-6 text-center">
          <h1 className="text-5xl font-bold">📊 Job Skill Tracker</h1>
          <p className="mt-3 text-lg">
            Analyze the most in-demand skills from live remote job postings
          </p>
        </div>
      </div>

      <div className="max-w-7xl mx-auto p-6">

        {/* Dashboard Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">

          <div className="bg-white rounded-2xl shadow-lg p-6 text-center">
            <h2 className="text-gray-500 text-lg">Total Jobs</h2>
            <p className="text-4xl font-bold text-blue-600">
              {jobs.length}
            </p>
          </div>

          <div className="bg-white rounded-2xl shadow-lg p-6 text-center">
            <h2 className="text-gray-500 text-lg">Skills Found</h2>
            <p className="text-4xl font-bold text-green-600">
              {skills.length}
            </p>
          </div>

          <div className="bg-white rounded-2xl shadow-lg p-6 text-center">
            <h2 className="text-gray-500 text-lg">Roles</h2>
            <p className="text-4xl font-bold text-purple-600">
              {roles.length}
            </p>
          </div>

        </div>

        {/* Chart Section */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8">

          <div className="flex flex-col md:flex-row md:justify-between md:items-center mb-6">

            <h2 className="text-3xl font-bold mb-4 md:mb-0">
              Top Skills
            </h2>

            <select
              className="border-2 border-gray-300 rounded-lg p-3 w-full md:w-80"
              value={selectedRole}
              onChange={(e) => setSelectedRole(e.target.value)}
            >
              <option value="">All Roles</option>

              {roles.map((role, index) => (
                <option key={index} value={role}>
                  {role}
                </option>
              ))}
            </select>

          </div>

          <ResponsiveContainer width="100%" height={450}>
            <BarChart data={skills}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis
                dataKey="Skill"
                angle={-45}
                textAnchor="end"
                interval={0}
                height={100}
              />
              <YAxis />
              <Tooltip />
              <Bar dataKey="Count" />
            </BarChart>
          </ResponsiveContainer>

        </div>

        {/* Jobs Section */}
        <div>

          <h2 className="text-3xl font-bold mb-6">
            Latest Jobs
          </h2>

          <div className="grid md:grid-cols-2 gap-6">

            {filteredJobs.map((job) => (

              <div
                key={job.id}
                className="bg-white rounded-2xl shadow-lg p-6 hover:shadow-2xl transition duration-300"
              >

                <h3 className="text-2xl font-bold mb-4">
                  {job.title}
                </h3>

                <p className="mb-2">
                  <strong>Company:</strong> {job.company}
                </p>

                <p className="mb-2">
                  <strong>Role:</strong> {job.role}
                </p>

                <p className="mb-2">
                  <strong>Location:</strong> {job.location}
                </p>

                <p className="mb-4">
                  <strong>Tags:</strong> {job.tags}
                </p>

                <a
                  href={job.url}
                  target="_blank"
                  rel="noreferrer"
                  className="inline-block bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-lg"
                >
                  View Job
                </a>

              </div>

            ))}

          </div>

        </div>

      </div>

      {/* Footer */}
      <footer className="bg-gray-900 text-white text-center py-6 mt-10">
        Built with ❤️ using React • FastAPI • SQLite • Pandas • Recharts
      </footer>

    </div>
  );
}

export default App;