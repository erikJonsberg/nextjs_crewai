'use client';

import { EventLog } from '@/components/EventLog';
import { FinalOutput } from '@/components/FinalOutput';
import InputSection from '@/components/InputSection';
import { useCrewJob } from '@/lib/useCrewJob';

export default function Home() {
	const crewJob = useCrewJob();

	return (
		<div className='bg-white min-h-screen text-black flex items-center justify-center flex-col'>
			<div className='flex items-center flex-col w-full'>
				<InputSection
					title='Companies'
					placeholder='Add a company'
					data={crewJob.companies}
					setData={crewJob.setCompanies}
				/>
				<InputSection
					title='Positions'
					placeholder='Add a position'
					data={crewJob.positions}
					setData={crewJob.setPositions}
				/>
			</div>
			<div className='flex justify-between items-center py-10'>
				<h2 className='text-2xl font-bold text-center mr-4'>Run Job</h2>
				<button
					onClick={() => crewJob.startJob()}
					className='bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-8 rounded text-base'
					disabled={crewJob.running}
				>
					{crewJob.running ? 'Running...' : 'Start'}
				</button>
			</div>
			<div className='w-1/2 p-4 flex flex-col'>
				<h2 className='text-2xl font-bold text-center'>Output</h2>
				<FinalOutput positionInfoList={crewJob.positionInfoList} />
				<EventLog events={crewJob.events} />
			</div>
		</div>
	);
}
