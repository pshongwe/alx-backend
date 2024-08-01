#!/usr/bin/node
import { createQueue } from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518782',
    message: 'This is the code 4563 to verify your account',
  },
  {
    phoneNumber: '4153518744',
    message: 'This is the code 4320 to verify your account',
  },
  {
    phoneNumber: '4153538779',
    message: 'This is the code 4262 to verify your account',
  },
  {
    phoneNumber: '4153118882',
    message: 'This is the code 4021 to verify your account',
  },
  {
    phoneNumber: '4153714780',
    message: 'This is the code 3562 to verify your account',
  },
  {
    phoneNumber: '4159514482',
    message: 'This is the code 1321 to verify your account',
  },
  {
    phoneNumber: '4158713381',
    message: 'This is the code 0562 to verify your account',
  },
  {
    phoneNumber: '4153818222',
    message: 'This is the code 0021 to verify your account',
  },
  {
    phoneNumber: '4154312281',
    message: 'This is the code 2262 to verify your account',
  },
  {
    phoneNumber: '4151244582',
    message: 'This is the code 4521 to verify your account',
  },
];

const queue = createQueue({ name: 'push_notification_code_2' });

for (const jobInfo of jobs) {
  const job = queue.create('push_notification_code_2', jobInfo);

  job
    .on('enqueue', () => {
      console.log('Notification job created:', job.id);
    })
    .on('complete', () => {
      console.log('Notification job', job.id, 'completed');
    })
    .on('failed', (err) => {
      console.log('Notification job', job.id, 'failed:', err.message || err.toString());
    })
    .on('progress', (progress, _data) => {
      console.log('Notification job', job.id, `${progress}% complete`);
    });
  job.save();
}
