import { render, screen } from '@testing-library/react';
import Dashboard from '../../frontend/dashboard/Dashboard';

test('renders dashboard header', () => {
  render(<Dashboard />);
  const header = screen.getByText(/LTD Dashboard/i);
  expect(header).toBeInTheDocument();
});
