import { EventType } from '@/lib/useCrewJob';

// This component will receive props to update events.
type EventLogProps = {
	events: EventType[];
};

export const EventLog: React.FC<EventLogProps> = ({ events }) => {
	return (
		<div className='flex flex-col h-full'>
			<h2 className='text-lg font-semibold mb-2'>Event Details</h2>
			<div className='flex-grow overflow-auto border-2 border-gray-100 p-2 min-h-64'>
				{events.length === 0 ? (
					<p>No events yet.</p>
				) : (
					events.map((event, index) => (
						<div
							key={index}
							className='p-2 border-b border-gray-200'
						>
							<p>
								{event.timestamp}: {event.data}
							</p>
						</div>
					))
				)}
			</div>
		</div>
	);
};
