import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import DataTable from './DataTable'
import reportWebVitals from './reportWebVitals';

//import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import AppBar from '@mui/material/AppBar';

import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';


ReactDOM.render(
  <React.StrictMode>
  <AppBar position="static" style={{backgroundColor: "#877ff4"}}>
  <Toolbar variant="dense" color="string">
    <IconButton edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
      <MenuIcon />
    </IconButton>
    <Typography variant="h6" color="inherit" component="div">
      Making NBA history
    </Typography>
  </Toolbar>
</AppBar>
    <Grid container spacing={8} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
  <Grid item xl={6} md={8}>
  </Grid>
  <Grid item xl={6} md={4}>
  </Grid>
  <Grid item xl={6} md={8}>
  <Card sx={{ maxWidth: 500, marginLeft : "15%", }}>
      <CardContent>
        <Typography sx={{ fontSize: 20 }} color="text.secondary" gutterBottom>
          Lebron James
        </Typography>
        <Typography variant="h6" component="div">
          How many points does he have? 
        </Typography>
        <Typography variant="h6" component="div"> 
          How many points does the other guy have?
        </Typography>
        <Typography variant="h6" component="div">
          How many games till he make it?
        </Typography>
        <Typography sx={{ mb: 0.5 }} color="text.secondary">
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Makena</Button>
      </CardActions>
    </Card>
  </Grid>
  <Grid item xl={6} md={4}>
  </Grid>
  <Grid item xs={6} md={4}>
  </Grid>
  <Grid item xs={6} md={8}>
      <Container maxWidth="sm" sx = {{marginTop:"-5%"}}>
        <DataTable />
      </Container>
  </Grid>
</Grid>
</React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
