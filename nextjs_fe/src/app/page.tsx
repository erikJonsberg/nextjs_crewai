import Header from '@/components/Header';
import EventLog from '@/components/EventLog';
import InputSection from '@/components/InputSection';
import FinalOutput from '@/components/FinalOutput';

export default function Home() {
	return (
		<main className='flex flex-col items-center justify-center min-h-screen py-2'>
			<Header />
			<EventLog />

			<InputSection />
			<FinalOutput />
			<h1 className='text-4xl text-center mt-20'>Home Page</h1>
		</main>
	);
}
